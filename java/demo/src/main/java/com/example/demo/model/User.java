package com.example.demo.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class User {
    
    @NotNull
    private Long id;
    
    @NotBlank(message = "Username cannot be blank")
    private String username;
    
    @NotBlank(message = "Email cannot be blank")
    private String email;
} 