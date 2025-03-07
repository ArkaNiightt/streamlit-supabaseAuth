from supabase import create_client, Client
from utils.config import DATABASE
import streamlit as st
import pandas as pd
from database.supabaseConection import inicializar_supabase


def check_login(email, password):
    supabase = inicializar_supabase()
    try:
        user = supabase.auth.sign_in_with_password(
            {"email": email, "password": password})
        if user:
            return True
    except Exception as e:
        print(f"Erro ao fazer login: {str(e)}")
    return False
