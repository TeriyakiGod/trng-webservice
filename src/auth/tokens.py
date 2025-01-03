from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Token generator for account activation
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Ensure the token is invalidated upon password change or email change
        return (
            str(user.pk) + str(timestamp) +
            str(user.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()

# Token generator for password reset
class PasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Ensure the token is invalidated upon password change
        return (
            str(user.pk) + str(timestamp) +
            str(user.password)
        )

password_reset_token = PasswordResetTokenGenerator()