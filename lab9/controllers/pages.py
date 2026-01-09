from jinja2 import Environment
from typing import Dict, Any

class PagesController:
    """Контроллер для рендеринга страниц"""

    def __init__(self, env: Environment):
        self.env = env

    def render_author(self, context: Dict[str, Any]) -> str:
        """Рендер author.html"""
        template = self.env.get_template("author.html")
        return template.render(**context)
    
    def render_currencies(self, context: Dict[str, Any]) -> str:
        """Рендер currencies.html"""
        template = self.env.get_template("currencies.html")
        return template.render(**context)

    def render_index(self, context: Dict[str, Any]) -> str:
        """Рендер index.html"""
        template = self.env.get_template("index.html")
        return template.render(**context)
    
    def render_user(self, context: Dict[str, Any]) -> str:
        """Рендер user.html"""
        template = self.env.get_template("user.html")
        return template.render(**context)

    def render_users(self, context: Dict[str, Any]) -> str:
        """Рендер users.html"""
        template = self.env.get_template("users.html")
        return template.render(**context)

