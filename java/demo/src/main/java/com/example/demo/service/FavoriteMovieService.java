package com.example.demo.service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArraySet;

import org.springframework.stereotype.Service;

import com.example.demo.model.Movie;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class FavoriteMovieService {
    
    // Using ConcurrentHashMap for thread-safe operations
    // Key: userId, Value: Set of favorite movie IDs
    private final ConcurrentHashMap<Long, CopyOnWriteArraySet<Long>> userFavorites = new ConcurrentHashMap<>();
    
    // Mock database for movies - using ConcurrentHashMap for thread safety
    private final ConcurrentHashMap<Long, Movie> movieDatabase = new ConcurrentHashMap<>();
    
    public FavoriteMovieService() {
        initializeSampleMovies();
    }
    
    /**
     * Like a movie - add to user's favorites
     */
    public boolean likeMovie(Long userId, Long movieId) {
        if (!movieDatabase.containsKey(movieId)) {
            log.warn("Movie with ID {} not found", movieId);
            return false;
        }
        
        userFavorites.computeIfAbsent(userId, k -> new CopyOnWriteArraySet<>()).add(movieId);
        log.info("User {} liked movie {}", userId, movieId);
        return true;
    }
    
    /**
     * Get list of user's favorite movies
     */
    public List<Movie> getUserFavoriteMovies(Long userId) {
        Set<Long> favoriteMovieIds = userFavorites.getOrDefault(userId, new CopyOnWriteArraySet<>());
        
        return favoriteMovieIds.stream()
                .map(movieDatabase::get)
                .filter(Objects::nonNull)
                .sorted(Comparator.comparing(Movie::getTitle))
                .toList();
    }
    
    /**
     * Remove a movie from user's favorites
     */
    public boolean removeFavoriteMovie(Long userId, Long movieId) {
        Set<Long> userFavoriteMovies = userFavorites.get(userId);
        if (userFavoriteMovies == null) {
            log.warn("User {} has no favorite movies", userId);
            return false;
        }
        
        boolean removed = userFavoriteMovies.remove(movieId);
        if (removed) {
            log.info("User {} removed movie {} from favorites", userId, movieId);
        } else {
            log.warn("Movie {} was not in user {}'s favorites", movieId, userId);
        }
        
        return removed;
    }
    
    /**
     * Check if a movie is in user's favorites
     */
    public boolean isMovieFavorite(Long userId, Long movieId) {
        Set<Long> userFavoriteMovies = userFavorites.get(userId);
        return userFavoriteMovies != null && userFavoriteMovies.contains(movieId);
    }
    
    /**
     * Get all available movies
     */
    public List<Movie> getAllMovies() {
        return new ArrayList<>(movieDatabase.values());
    }
    
    /**
     * Get movie by ID
     */
    public Optional<Movie> getMovieById(Long movieId) {
        return Optional.ofNullable(movieDatabase.get(movieId));
    }
    
    /**
     * Rate a movie (update star rating)
     */
    public boolean rateMovie(Long movieId, Integer starRating) {
        if (starRating < 1 || starRating > 5) {
            log.warn("Invalid star rating: {}. Must be between 1 and 5", starRating);
            return false;
        }
        
        Movie movie = movieDatabase.get(movieId);
        if (movie == null) {
            log.warn("Movie with ID {} not found", movieId);
            return false;
        }
        
        movie.setStarRating(starRating);
        log.info("Movie {} rated with {} stars", movieId, starRating);
        return true;
    }
    
    /**
     * Initialize sample movies for testing
     */
    private void initializeSampleMovies() {
        List<Movie> sampleMovies = Arrays.asList(
            Movie.builder()
                .id(1L)
                .title("The Matrix")
                .description("A computer programmer discovers reality is a simulation")
                .type(Movie.MovieType.MOVIE)
                .genre("Sci-Fi")
                .releaseYear(1999)
                .starRating(5)
                .build(),
            Movie.builder()
                .id(2L)
                .title("Breaking Bad")
                .description("A high school chemistry teacher turns to manufacturing drugs")
                .type(Movie.MovieType.SERIES)
                .genre("Drama")
                .releaseYear(2008)
                .starRating(5)
                .build(),
            Movie.builder()
                .id(3L)
                .title("Inception")
                .description("A thief enters people's dreams to steal secrets")
                .type(Movie.MovieType.MOVIE)
                .genre("Sci-Fi")
                .releaseYear(2010)
                .starRating(4)
                .build(),
            Movie.builder()
                .id(4L)
                .title("Stranger Things")
                .description("Kids encounter supernatural forces in their small town")
                .type(Movie.MovieType.SERIES)
                .genre("Horror/Sci-Fi")
                .releaseYear(2016)
                .starRating(4)
                .build(),
            Movie.builder()
                .id(5L)
                .title("The Godfather")
                .description("The patriarch of an organized crime dynasty")
                .type(Movie.MovieType.MOVIE)
                .genre("Crime")
                .releaseYear(1972)
                .starRating(5)
                .build()
        );
        
        sampleMovies.forEach(movie -> movieDatabase.put(movie.getId(), movie));
        log.info("Initialized {} sample movies", sampleMovies.size());
    }
} 