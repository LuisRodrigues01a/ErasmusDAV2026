def create_email_message(subject, body, *, sender="notification@example.com", **kwargs):
    message = {"subject": subject, "body": body, "sender": sender}
    message.update(kwargs)
    return message

print(create_email_message("Hello", "How are you?"))
print(create_email_message("Meeting", "Tomorrow at 10am", sender="boss@company.com"))
print(create_email_message("Task", "Finish the report", priority="high", category="work", deadline="Friday"))