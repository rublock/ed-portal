from pathlib import Path
from time import time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
#фреймворк перевода
from django.utils.translation import gettext_lazy as _

# функция которая возвращает путь к файлу и имя файла аватарки в формате вермени в юникод
# instance — экземпляр класса модели пользователя
# filename — имя загруженного файла
# формат файла pic_1702039183
def users_avatars_path(instance, filename):
    # файл будет загружен в:
    # MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return "user_{0}/avatars/{1}".format(instance.username, f"pic_{num}{suff}")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        #проверка имени пользователя на символы -*/!@#$%^&*() и т.д.
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    #этого поля например нет в стандартной модели
    age = models.PositiveIntegerField(blank=True, null=True)
    # поле для аватарки
    avatar = models.ImageField(upload_to=users_avatars_path, blank=True, null=True)
    email = models.CharField(
        _("email address"),
        max_length=256,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    #стандатный менеджер модели, для модели пользователя
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    #как мы будем видеть поля в админке
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # метод для нормализации e-mail
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # полное имя пользователя имя, фамилия через пробел
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    # только имя
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    # отправить пользователю письмо по e-mail
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)