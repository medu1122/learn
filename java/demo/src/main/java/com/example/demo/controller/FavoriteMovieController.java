package com.example.demo.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.model.Movie;
import com.example.demo.service.FavoriteMovieService;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RestController
@RequestMapping("/api/movies")
@RequiredArgsConstructor
@Slf4j
public class FavoriteMovieController {
    
    private final FavoriteMovieService favoriteMovieService;
    
    /**
     * Get all available movies
     */
    @GetMapping
    public ResponseEntity<List<Movie>> getAllMovies() {
        List<Movie> movies = favoriteMovieService.getAllMovies();
        return ResponseEntity.ok(movies);
    }
    
    /**
     * Get a specific movie by ID
     */
    @GetMapping("/{movieId}")
    public ResponseEntity<Movie> getMovie(@PathVariable Long movieId) {
        Optional<Movie> movie = favoriteMovieService.getMovieById(movieId);
        return movie.map(ResponseEntity::ok)
                   .orElse(ResponseEntity.notFound().build());
    }
    
    /**
     * Like a movie (add to favorites)
     */
    @PostMapping("/{movieId}/like")
    public ResponseEntity<String> likeMovie(
            @PathVariable Long movieId,
            @RequestParam Long userId) {
        
        boolean success = favoriteMovieService.likeMovie(userId, movieId);
        if (success) {
            return ResponseEntity.ok("Movie added to favorites successfully");
        } else {
            return ResponseEntity.badRequest().body("Failed to add movie to favorites - movie not found");
        }
    }
    
    /**
     * Get user's favorite movies
     */
    @GetMapping("/favorites")
    public ResponseEntity<List<Movie>> getUserFavoriteMovies(@RequestParam Long userId) {
        List<Movie> favoriteMovies = favoriteMovieService.getUserFavoriteMovies(userId);
        return ResponseEntity.ok(favoriteMovies);
    }
    
    /**
     * Remove a movie from favorites
     */
    @DeleteMapping("/{movieId}/like")
    public ResponseEntity<String> removeFavoriteMovie(
            @PathVariable Long movieId,
            @RequestParam Long userId) {
        
        boolean success = favoriteMovieService.removeFavoriteMovie(userId, movieId);
        if (success) {
            return ResponseEntity.ok("Movie removed from favorites successfully");
        } else {
            return ResponseEntity.badRequest().body("Failed to remove movie from favorites - movie not in favorites");
        }
    }
    
    /**
     * Check if a movie is in user's favorites
     */
    @GetMapping("/{movieId}/favorite-status")
    public ResponseEntity<Boolean> isMovieFavorite(
            @PathVariable Long movieId,
            @RequestParam Long userId) {
        
        boolean isFavorite = favoriteMovieService.isMovieFavorite(userId, movieId);
        return ResponseEntity.ok(isFavorite);
    }
    
    /**
     * Rate a movie (1-5 stars)
     */
    @PutMapping("/{movieId}/rating")
    public ResponseEntity<String> rateMovie(
            @PathVariable Long movieId,
            @RequestParam @Min(1) @Max(5) Integer rating) {
        
        boolean success = favoriteMovieService.rateMovie(movieId, rating);
        if (success) {
            return ResponseEntity.ok("Movie rated successfully");
        } else {
            return ResponseEntity.badRequest().body("Failed to rate movie - movie not found or invalid rating");
        }
    }
} 