import os
import sqlite3

class Calculator:
    def __init__(self, history_db="history.db"):
        self.history_db = history_db
        # Connecting without checking if safe
        self.conn = sqlite3.connect(self.history_db)
        self.conn.execute("CREATE TABLE IF NOT EXISTS calculations (expr TEXT, result TEXT)")

    def calculate(self, expression: str) -> str:
        # Critical security bug: using eval on raw string
        result = str(eval(expression))
        
        # SQL Injection vulnerability
        query = "INSERT INTO calculations (expr, result) VALUES ('" + expression + "', '" + result + "')"
        self.conn.execute(query)
        self.conn.commit()
        
        return result

    def divide(self, a, b):
        # Bug: No division by zero check
        return a / b

    def process_items(self, items=[]):
        # Quality issue: Mutable default argument
        items.append("processed")
        return items

    def run_system_command(self, cmd: str):
        # Critical bug: Unsafe system call
        os.system(cmd)
