package com.example.demo.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Movie {
    
    @NotNull
    private Long id;
    
    @NotBlank(message = "Title cannot be blank")
    private String title;
    
    @NotBlank(message = "Description cannot be blank")
    private String description;
    
    @NotNull
    private MovieType type; // MOVIE or SERIES
    
    private String genre;
    
    private Integer releaseYear;
    
    @Min(value = 1, message = "Rating must be between 1 and 5")
    @Max(value = 5, message = "Rating must be between 1 and 5")
    private Integer starRating; // 1-5 stars
    
    public enum MovieType {
        MOVIE, SERIES
    }
} 