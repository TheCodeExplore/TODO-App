import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QListWidget, 
    QPushButton, QLineEdit, QMessageBox
)

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیمات اولیه پنجره اصلی
        self.setWindowTitle("اپلیکیشن لیست وظایف")
        self.setGeometry(300, 300, 400, 300)

        # ویجت مرکزی و تنظیمات آن
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # تعریف لایه‌بندی اصلی
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # ایجاد لیست وظایف
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # لایه‌بندی افقی برای ورودی و دکمه‌ها
        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)

        # ورودی متن برای افزودن وظیفه جدید
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("وظیفه جدید را وارد کنید...")
        self.input_layout.addWidget(self.task_input)

        # دکمه افزودن وظیفه
        self.add_button = QPushButton("افزودن وظیفه")
        self.add_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.add_button)

        # دکمه حذف وظیفه انتخاب‌شده
        self.remove_button = QPushButton("حذف وظیفه انتخابی")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

    def add_task(self):
        """اضافه کردن وظیفه جدید به لیست."""
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "هشدار", "وظیفه نمی‌تواند خالی باشد!")

    def remove_task(self):
        """حذف وظیفه انتخابی از لیست."""
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            QMessageBox.warning(self, "هشدار", "هیچ وظیفه‌ای انتخاب نشده است!")

# تابع اصلی برای اجرای برنامه
def main():
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
