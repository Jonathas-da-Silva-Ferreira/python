import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests

API_URL = "http://127.0.0.1:8000/api/tasks/"

class TaskApp(ctk.CTK):
    def __init__(self):
        super().__init__()

        self.title("TO-DO List")