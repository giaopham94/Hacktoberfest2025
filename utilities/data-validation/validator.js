/**
 * A utility class for common data validation tasks
 */
class DataValidator {
    /**
     * Validates an email address
     * @param {string} email - The email address to validate
     * @returns {boolean} - True if email is valid, false otherwise
     */
    static isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    /**
     * Validates if a string contains only letters and spaces
     * @param {string} text - The text to validate
     * @returns {boolean} - True if text contains only letters and spaces
     */
    static isValidName(text) {
        const nameRegex = /^[A-Za-z\s]+$/;
        return nameRegex.test(text);
    }

    /**
     * Checks if a password meets minimum security requirements
     * - At least 8 characters
     * - Contains at least one uppercase letter
     * - Contains at least one lowercase letter
     * - Contains at least one number
     * - Contains at least one special character
     * @param {string} password - The password to validate
     * @returns {boolean} - True if password meets all requirements
     */
    static isStrongPassword(password) {
        const minLength = 8;
        const hasUpperCase = /[A-Z]/.test(password);
        const hasLowerCase = /[a-z]/.test(password);
        const hasNumbers = /\d/.test(password);
        const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        return password.length >= minLength &&
            hasUpperCase &&
            hasLowerCase &&
            hasNumbers &&
            hasSpecialChar;
    }

    /**
     * Validates if a string is a valid date in YYYY-MM-DD format
     * @param {string} dateString - The date string to validate
     * @returns {boolean} - True if date is valid
     */
    static isValidDate(dateString) {
        const date = new Date(dateString);
        return date instanceof Date && !isNaN(date) &&
            dateString.match(/^\d{4}-\d{2}-\d{2}$/);
    }
}

module.exports = DataValidator;
