from django.db import models


class Image(models.Model):
    caption = models.CharField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to="img/%y")
    created_at_utc = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.caption}({self.created_at_utc})"

    class Meta:
        db_table = "Image"
        ordering = ("-created_at_utc",)
