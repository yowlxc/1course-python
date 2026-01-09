"""Тесты для DatabaseController."""

import unittest
from controllers.databasecontroller import DatabaseController


class TestDatabaseController(unittest.TestCase):
    """Тесты работы с базой данных."""

    def setUp(self):
        """Создаёт новую БД перед каждым тестом."""
        self.db = DatabaseController()

    def tearDown(self):
        """Закрывает соединение после теста."""
        self.db.close()

    def test_get_all_users(self):
        """Проверка получения списка пользователей."""
        users = self.db.get_all_users()
        self.assertGreater(len(users), 0)
        self.assertIn("Настя Пирогова", [u["name"] for u in users])

    def test_add_and_remove_subscription(self):
        """Проверка добавления и удаления подписки."""
        # Добавляем подписку
        success = self.db.add_subscription(user_id=1, currency_id=1)
        self.assertTrue(success)

        # Проверяем, что подписка появилась
        subs = self.db.get_user_subscriptions(1)
        self.assertGreater(len(subs), 0)

        # Удаляем подписку
        removed = self.db.remove_subscription(user_id=1, currency_id=1)
        self.assertTrue(removed)

        # Проверяем, что подписки больше нет
        subs_after = self.db.get_user_subscriptions(1)
        self.assertEqual(len(subs_after), len(subs) - 1)

    def test_delete_currency_with_subscriptions(self):
        """Удаление валюты, на которую есть подписки (с ON DELETE CASCADE)."""
        # Убеждаемся, что у пользователя 1 есть подписка на валюту 2
        subs_before = self.db.get_user_subscriptions(1)
        has_eur = any(c["id"] == 2 for c in subs_before)
        self.assertTrue(has_eur)

        # Удаляем валюту EUR (id=2)
        deleted = self.db.delete_currency(2)
        self.assertTrue(deleted)

        # Проверяем, что подписка исчезла
        subs_after = self.db.get_user_subscriptions(1)
        has_eur_after = any(c["id"] == 2 for c in subs_after)
        self.assertFalse(has_eur_after)

if __name__ == "__main__":
    unittest.main(verbosity=2)