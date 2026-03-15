# Data Validation Utility

This utility provides a set of commonly used data validation functions that can be used across the project.

## Features

- Email validation
- Name validation (letters and spaces only)
- Strong password validation
- Date format validation (YYYY-MM-DD)

## Usage

```javascript
const DataValidator = require('./validator');

// Validate email
console.log(DataValidator.isValidEmail('user@example.com')); // true
console.log(DataValidator.isValidEmail('invalid-email')); // false

// Validate name
console.log(DataValidator.isValidName('John Doe')); // true
console.log(DataValidator.isValidName('John123')); // false

// Check password strength
console.log(DataValidator.isStrongPassword('Abcd123!@')); // true
console.log(DataValidator.isStrongPassword('weak')); // false

// Validate date
console.log(DataValidator.isValidDate('2025-10-14')); // true
console.log(DataValidator.isValidDate('2025/10/14')); // false
```

## Contributing

Feel free to add more validation functions or improve the existing ones!
