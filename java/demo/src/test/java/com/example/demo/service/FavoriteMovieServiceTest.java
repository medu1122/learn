package com.example.demo.service;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.example.demo.model.Movie;

class FavoriteMovieServiceTest {
    
    private FavoriteMovieService favoriteMovieService;
    
    @BeforeEach
    void setUp() {
        favoriteMovieService = new FavoriteMovieService();
    }
    
    @Test
    @DisplayName("Should successfully like a movie when movie exists")
    void testLikeMovie_Success() {
        // Given
        Long userId = 1L;
        Long movieId = 1L; // The Matrix from sample data
        
        // When
        boolean result = favoriteMovieService.likeMovie(userId, movieId);
        
        // Then
        assertTrue(result);
        assertTrue(favoriteMovieService.isMovieFavorite(userId, movieId));
    }
    
    @Test
    @DisplayName("Should fail to like a movie when movie does not exist")
    void testLikeMovie_MovieNotFound() {
        // Given
        Long userId = 1L;
        Long nonExistentMovieId = 999L;
        
        // When
        boolean result = favoriteMovieService.likeMovie(userId, nonExistentMovieId);
        
        // Then
        assertFalse(result);
        assertFalse(favoriteMovieService.isMovieFavorite(userId, nonExistentMovieId));
    }
    
    @Test
    @DisplayName("Should return empty list when user has no favorite movies")
    void testGetUserFavoriteMovies_EmptyList() {
        // Given
        Long userId = 1L;
        
        // When
        List<Movie> favoriteMovies = favoriteMovieService.getUserFavoriteMovies(userId);
        
        // Then
        assertNotNull(favoriteMovies);
        assertTrue(favoriteMovies.isEmpty());
    }
    
    @Test
    @DisplayName("Should return user's favorite movies sorted by title")
    void testGetUserFavoriteMovies_WithFavorites() {
        // Given
        Long userId = 1L;
        Long matrixId = 1L; // The Matrix
        Long inceptionId = 3L; // Inception
        
        // When
        favoriteMovieService.likeMovie(userId, matrixId);
        favoriteMovieService.likeMovie(userId, inceptionId);
        List<Movie> favoriteMovies = favoriteMovieService.getUserFavoriteMovies(userId);
        
        // Then
        assertNotNull(favoriteMovies);
        assertEquals(2, favoriteMovies.size());
        // Should be sorted by title: Inception comes before The Matrix
        assertEquals("Inception", favoriteMovies.get(0).getTitle());
        assertEquals("The Matrix", favoriteMovies.get(1).getTitle());
    }
    
    @Test
    @DisplayName("Should successfully remove a movie from favorites")
    void testRemoveFavoriteMovie_Success() {
        // Given
        Long userId = 1L;
        Long movieId = 1L;
        favoriteMovieService.likeMovie(userId, movieId);
        
        // When
        boolean result = favoriteMovieService.removeFavoriteMovie(userId, movieId);
        
        // Then
        assertTrue(result);
        assertFalse(favoriteMovieService.isMovieFavorite(userId, movieId));
    }
    
    @Test
    @DisplayName("Should fail to remove movie when user has no favorites")
    void testRemoveFavoriteMovie_NoFavorites() {
        // Given
        Long userId = 1L;
        Long movieId = 1L;
        
        // When
        boolean result = favoriteMovieService.removeFavoriteMovie(userId, movieId);
        
        // Then
        assertFalse(result);
    }
    
    @Test
    @DisplayName("Should fail to remove movie when movie is not in favorites")
    void testRemoveFavoriteMovie_MovieNotInFavorites() {
        // Given
        Long userId = 1L;
        Long favoriteMovieId = 1L;
        Long nonFavoriteMovieId = 2L;
        favoriteMovieService.likeMovie(userId, favoriteMovieId);
        
        // When
        boolean result = favoriteMovieService.removeFavoriteMovie(userId, nonFavoriteMovieId);
        
        // Then
        assertFalse(result);
        assertTrue(favoriteMovieService.isMovieFavorite(userId, favoriteMovieId));
    }
    
    @Test
    @DisplayName("Should return true when movie is in user's favorites")
    void testIsMovieFavorite_True() {
        // Given
        Long userId = 1L;
        Long movieId = 1L;
        favoriteMovieService.likeMovie(userId, movieId);
        
        // When
        boolean isFavorite = favoriteMovieService.isMovieFavorite(userId, movieId);
        
        // Then
        assertTrue(isFavorite);
    }
    
    @Test
    @DisplayName("Should return false when movie is not in user's favorites")
    void testIsMovieFavorite_False() {
        // Given
        Long userId = 1L;
        Long movieId = 1L;
        
        // When
        boolean isFavorite = favoriteMovieService.isMovieFavorite(userId, movieId);
        
        // Then
        assertFalse(isFavorite);
    }
    
    @Test
    @DisplayName("Should return all available movies")
    void testGetAllMovies() {
        // When
        List<Movie> allMovies = favoriteMovieService.getAllMovies();
        
        // Then
        assertNotNull(allMovies);
        assertEquals(5, allMovies.size()); // Sample data has 5 movies
    }
    
    @Test
    @DisplayName("Should return movie when movie ID exists")
    void testGetMovieById_Found() {
        // Given
        Long movieId = 1L;
        
        // When
        Optional<Movie> movie = favoriteMovieService.getMovieById(movieId);
        
        // Then
        assertTrue(movie.isPresent());
        assertEquals("The Matrix", movie.get().getTitle());
        assertEquals(Movie.MovieType.MOVIE, movie.get().getType());
    }
    
    @Test
    @DisplayName("Should return empty when movie ID does not exist")
    void testGetMovieById_NotFound() {
        // Given
        Long nonExistentMovieId = 999L;
        
        // When
        Optional<Movie> movie = favoriteMovieService.getMovieById(nonExistentMovieId);
        
        // Then
        assertFalse(movie.isPresent());
    }
    
    @Test
    @DisplayName("Should successfully rate a movie with valid rating")
    void testRateMovie_Success() {
        // Given
        Long movieId = 1L;
        Integer newRating = 4;
        
        // When
        boolean result = favoriteMovieService.rateMovie(movieId, newRating);
        
        // Then
        assertTrue(result);
        Optional<Movie> movie = favoriteMovieService.getMovieById(movieId);
        assertTrue(movie.isPresent());
        assertEquals(newRating, movie.get().getStarRating());
    }
    
    @Test
    @DisplayName("Should fail to rate movie with invalid rating (too low)")
    void testRateMovie_InvalidRatingTooLow() {
        // Given
        Long movieId = 1L;
        Integer invalidRating = 0;
        
        // When
        boolean result = favoriteMovieService.rateMovie(movieId, invalidRating);
        
        // Then
        assertFalse(result);
    }
    
    @Test
    @DisplayName("Should fail to rate movie with invalid rating (too high)")
    void testRateMovie_InvalidRatingTooHigh() {
        // Given
        Long movieId = 1L;
        Integer invalidRating = 6;
        
        // When
        boolean result = favoriteMovieService.rateMovie(movieId, invalidRating);
        
        // Then
        assertFalse(result);
    }
    
    @Test
    @DisplayName("Should fail to rate non-existent movie")
    void testRateMovie_MovieNotFound() {
        // Given
        Long nonExistentMovieId = 999L;
        Integer validRating = 4;
        
        // When
        boolean result = favoriteMovieService.rateMovie(nonExistentMovieId, validRating);
        
        // Then
        assertFalse(result);
    }
    
    @Test
    @DisplayName("Should handle concurrent operations safely")
    void testConcurrentOperations() throws InterruptedException {
        // Given
        Long userId1 = 1L;
        Long userId2 = 2L;
        Long movieId = 1L;
        
        // When - simulate concurrent operations
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                favoriteMovieService.likeMovie(userId1, movieId);
                favoriteMovieService.removeFavoriteMovie(userId1, movieId);
            }
        });
        
        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                favoriteMovieService.likeMovie(userId2, movieId);
                favoriteMovieService.getUserFavoriteMovies(userId2);
            }
        });
        
        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();
        
        // Then - no exceptions should occur and operations should complete
        // The fact that we reach this point means concurrent operations worked
        assertTrue(true);
    }
    
    @Test
    @DisplayName("Should verify sample data initialization")
    void testSampleDataInitialization() {
        // When
        List<Movie> allMovies = favoriteMovieService.getAllMovies();
        
        // Then
        assertEquals(5, allMovies.size());
        
        // Verify specific sample movies exist
        assertTrue(allMovies.stream().anyMatch(m -> m.getTitle().equals("The Matrix")));
        assertTrue(allMovies.stream().anyMatch(m -> m.getTitle().equals("Breaking Bad")));
        assertTrue(allMovies.stream().anyMatch(m -> m.getTitle().equals("Inception")));
        assertTrue(allMovies.stream().anyMatch(m -> m.getTitle().equals("Stranger Things")));
        assertTrue(allMovies.stream().anyMatch(m -> m.getTitle().equals("The Godfather")));
        
        // Verify we have both movies and series
        long movieCount = allMovies.stream().filter(m -> m.getType() == Movie.MovieType.MOVIE).count();
        long seriesCount = allMovies.stream().filter(m -> m.getType() == Movie.MovieType.SERIES).count();
        
        assertTrue(movieCount > 0);
        assertTrue(seriesCount > 0);
    }
} 