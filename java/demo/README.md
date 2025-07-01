# Movie Favorites Management System

A Spring Boot application that allows users to manage their favorite movies and TV series using Java concurrency collections.

## Features Implemented

### Core Requirements ✅
- ✅ **Like 1 favorite movie** - Users can add movies to their favorites
- ✅ **List favorite movies** - Users can retrieve their favorite movies list  
- ✅ **Delete 1 movie from favorites** - Users can remove movies from their favorites
- ✅ **Unit Tests** - Comprehensive test coverage for all functionality
- ✅ **Lombok usage** - Used for generating code for models

### Enhanced Features ✅
- ✅ **Movies and Series support** - Content can be either movies or TV series
- ✅ **Star rating system** - Users can rate content from 1-5 stars

### Technical Implementation
- ✅ **Java Concurrency Collections** - Uses `ConcurrentHashMap` and `CopyOnWriteArraySet` for thread-safe operations
- ✅ **Spring Boot with Gradle** - Built using Gradle build tool
- ✅ **REST API endpoints** - Complete REST API for all operations
- ✅ **Data validation** - Input validation using Jakarta validation

## Technology Stack

- **Java 17**
- **Spring Boot 3.5.3** 
- **Spring Web** - REST API endpoints
- **Lombok** - Code generation for models
- **Gradle** - Build tool
- **JUnit 5** - Unit testing framework

## Concurrency Features

The application uses Java concurrency collections to ensure thread-safe operations:

- `ConcurrentHashMap<Long, CopyOnWriteArraySet<Long>>` for storing user favorites
- `ConcurrentHashMap<Long, Movie>` for the movie database
- `CopyOnWriteArraySet<Long>` for individual user's favorite movie IDs

This ensures the application can handle multiple users concurrently without data corruption.

## API Endpoints

### Get All Movies
```
GET /api/movies
```
Returns all available movies and series.

### Get Specific Movie
```
GET /api/movies/{movieId}
```
Returns details of a specific movie.

### Like a Movie (Add to Favorites)
```
POST /api/movies/{movieId}/like?userId={userId}
```
Adds a movie to user's favorites.

### Get User's Favorite Movies
```
GET /api/movies/favorites?userId={userId}
```
Returns all movies in user's favorites, sorted by title.

### Remove from Favorites
```
DELETE /api/movies/{movieId}/like?userId={userId}
```
Removes a movie from user's favorites.

### Check Favorite Status
```
GET /api/movies/{movieId}/favorite-status?userId={userId}
```
Returns whether a movie is in user's favorites.

### Rate a Movie
```
PUT /api/movies/{movieId}/rating?rating={1-5}
```
Updates the star rating for a movie (1-5 stars).

## Sample Data

The application comes with 5 pre-loaded movies and series:

1. **The Matrix** (Movie) - Sci-Fi, 1999, 5 stars
2. **Breaking Bad** (Series) - Drama, 2008, 5 stars  
3. **Inception** (Movie) - Sci-Fi, 2010, 4 stars
4. **Stranger Things** (Series) - Horror/Sci-Fi, 2016, 4 stars
5. **The Godfather** (Movie) - Crime, 1972, 5 stars

## Model Classes

### Movie
```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Movie {
    private Long id;
    private String title;
    private String description;
    private MovieType type; // MOVIE or SERIES
    private String genre;
    private Integer releaseYear;
    private Integer starRating; // 1-5 stars
    
    public enum MovieType {
        MOVIE, SERIES
    }
}
```

### User
```java
@Data
@Builder  
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private Long id;
    private String username;
    private String email;
}
```

## Running the Application

### Build the Project
```bash
./gradlew build
```

### Run the Application  
```bash
./gradlew bootRun
```

The application will start on `http://localhost:8080`

### Run Tests
```bash
./gradlew test
```

## Testing the APIs

### Example API Calls

1. **Get all movies:**
```bash
curl -X GET http://localhost:8080/api/movies
```

2. **Like a movie:**
```bash
curl -X POST "http://localhost:8080/api/movies/1/like?userId=1"
```

3. **Get user favorites:**
```bash
curl -X GET "http://localhost:8080/api/movies/favorites?userId=1"
```

4. **Remove from favorites:**
```bash
curl -X DELETE "http://localhost:8080/api/movies/1/like?userId=1"
```

5. **Rate a movie:**
```bash
curl -X PUT "http://localhost:8080/api/movies/1/rating?rating=5"
```

## Test Coverage

The application includes comprehensive unit tests covering:

- ✅ **Service layer tests** - All business logic methods
- ✅ **Concurrency testing** - Thread-safe operations verification
- ✅ **Edge cases** - Invalid inputs, non-existent data
- ✅ **Data validation** - Input validation scenarios
- ✅ **Sample data verification** - Correct initialization

### Test Scenarios Covered:

- Like/unlike movies successfully
- Handle non-existent movies/users
- List favorites (empty and populated)
- Remove movies from favorites
- Rate movies with valid/invalid ratings
- Concurrent operations safety
- Sample data initialization verification

## Project Structure

```
src/
├── main/
│   └── java/
│       └── com/example/demo/
│           ├── DemoApplication.java
│           ├── controller/
│           │   └── FavoriteMovieController.java
│           ├── model/
│           │   ├── Movie.java
│           │   └── User.java
│           └── service/
│               └── FavoriteMovieService.java
└── test/
    └── java/
        └── com/example/demo/
            └── service/
                └── FavoriteMovieServiceTest.java
```

## Key Features Highlights

### Concurrency Safety
- Thread-safe collections ensure data integrity
- Multiple users can operate simultaneously
- No race conditions or data corruption

### Validation
- Input validation for ratings (1-5 stars)
- Movie existence checks
- User operation validations

### Scalability  
- In-memory storage with concurrent collections
- Efficient lookups and operations
- Ready for database integration

### Clean Architecture
- Separation of concerns (Controller → Service → Model)
- Proper error handling and logging
- RESTful API design

This implementation fulfills all the assignment requirements including the use of Spring Boot with Gradle, Java concurrency collections, Lombok for code generation, comprehensive unit tests, and support for both movies and series with star ratings. 