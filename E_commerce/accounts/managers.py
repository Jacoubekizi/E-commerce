from django.contrib.auth.models import BaseUserManager

class CustomManagers(BaseUserManager):
    def _create_user(self, email, username, password=None, **extrafileds):
        if not email:
            raise ValueError("the give email must be set")
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            **extrafileds
        )
        user.set_password(password)
        user.save(using = self._db)

    def create_user(self, email, username, password=None, **extrafileds):
        extrafileds.setdefault("is_superuser", False)
        extrafileds.setdefault("is_staff", False)
        return self._create_user(email, username, password, **extrafileds)
    
    def create_superuser(self, email, username, password, **extrafileds):
        extrafileds.setdefault("is_superuser", True)
        extrafileds.setdefault("is_staff", True)

        if extrafileds.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superus=True")
        if extrafileds.get("is_staff") is not True:
            raise ValueError("Superuser must have is is_staff=True")
        
        return self._create_user(email, username, password, **extrafileds)