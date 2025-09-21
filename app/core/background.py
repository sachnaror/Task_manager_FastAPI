from fastapi import BackgroundTasks
import time


# --- Example background task: sending email ---
def send_email_notification(email: str, message: str):
    """
    Simulate sending an email (replace with real SMTP or API later).
    """
    # Simulate delay
    time.sleep(1)
    print(f"📧 Email sent to {email}: {message}")


def schedule_email(background_tasks: BackgroundTasks, email: str, message: str):
    """
    Schedule an email to be sent in the background.
    """
    background_tasks.add_task(send_email_notification, email, message)


# --- Example background task: logging ---
def log_event(event: str):
    """
    Log an event asynchronously.
    """
    print(f"📝 Log: {event}")


def schedule_log(background_tasks: BackgroundTasks, event: str):
    """
    Schedule a log entry.
    """
    background_tasks.add_task(log_event, event)


# --- Example background task: cleanup ---
def cleanup_temp_file(file_path: str):
    """
    Delete or clean up a temp file (simulate with print).
    """
    print(f"🧹 Cleaning up {file_path}")


def schedule_cleanup(background_tasks: BackgroundTasks, file_path: str):
    """
    Schedule file cleanup.
    """
    background_tasks.add_task(cleanup_temp_file, file_path)
