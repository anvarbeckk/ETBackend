from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('pre_intermediate', 'Pre-Intermediate'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper Intermediate'),
        ('advanced', 'Advanced'),
        ('proficient', 'Proficient'),
    ]
    content = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.get_level_display()}: {self.content[:50]}..."

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{'Correct' if self.is_correct else 'Incorrect'}: {self.content[:50]}..."
