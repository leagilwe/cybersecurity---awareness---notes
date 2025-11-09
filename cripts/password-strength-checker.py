import re
import getpass

def check_password_strength(password):
    """
    Check the strength of a password based on various criteria.
    Returns a score and feedback for improvement.
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("❌ Password should be at least 12 characters")
    
    # Complexity checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase letters")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include lowercase letters")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include numbers")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Include special characters")
    
    # Strength assessment
    if score >= 4:
        feedback.append("✅ Strong password!")
    elif score >= 3:
        feedback.append("⚠️  Moderate password - consider improving")
    else:
        feedback.append("🚨 Weak password - please strengthen")
    
    return score, feedback

if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    print("This tool helps assess your password security.")
    print("Note: Your password is not stored or transmitted.\n")
    
    password = getpass.getpass("Enter password to check: ")
    score, feedback = check_password_strength(password)
    
    print(f"\nStrength Score: {score}/5")
    print("Recommendations:")
    for item in feedback:
        print(f"  {item}")
