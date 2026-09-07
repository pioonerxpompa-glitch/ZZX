import sys
import subprocess

@app.post("/restart-serwera", response_class=HTMLResponse)
def restart_serwera():
    if current_session_user_id is None:
        return RedirectResponse(url="/", status_code=303)
    
    # Pobieramy dane aktualnego użytkownika, aby upewnić się, że to ADMIN
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (current_session_user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not user or user['role'] != 'ADMIN':
        return RedirectResponse(url="/?message=Brak uprawnień!&is_error=true", status_code=303)
    
    try:
        # Metoda bezpiecznego restartu procesu Pythona (działa na Windowsie i Linuxie)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    except Exception as e:
        return RedirectResponse(url=f"/?message=Błąd restartu: {e}&is_error=true", status_code=303)