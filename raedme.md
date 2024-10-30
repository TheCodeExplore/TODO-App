# اپلیکیشن لیست وظایف (To-Do List App) با PySide6 🗑️

[![Python](https://img.shields.io/badge/Language-Python-blue)](README.md) [![Persian](https://img.shields.io/badge/Language-فارسی-green)](README.fa.md)

این پروژه یک اپلیکیشن ساده برای مدیریت وظایف روزانه با استفاده از PySide6 و Python است.

## فهرست مطالب

- [✨ ویژگی‌ها](#-ویژگیها)
- [🚠 نصب](#️-نصب)
- [🚀 اجرا](#-اجرا)
- [📚 نحوه استفاده](#-نحوه-استفاده)
- [🗂️ ساختار پروژه](#️-ساختار-پروژه)
- [💻 کد اصلی](#-کد-اصلی)
- [📜 مجوز](#-مجوز)
- [📨 ارتباط با ما](#-ارتباط-با-ما)
- [🙏 سپاسگزاری](#-سپاسگزاری)
- [🌐 انتخاب زبان](#-انتخاب-زبان)

## ✨ ویژگی‌ها

- **اضافه کردن وظایف جدید**
- **حذف وظایف انتخابی**
- **نمایش لیست وظایف**
- **رابط کاربری ساده و کاربرپسند**
- **قابل اجرا در سیستم‌عامل‌های مختلف**

## 🚠 نصب

1. **نصب Python و PySide6:**

    ابتدا مطمئن شوید که Python 3.x روی سیستم شما نصب است. سپس PySide6 را با دستور زیر نصب کنید:

    ```bash
    pip install PySide6
    ```

2. **کلون کردن ریپوزیتوری:**

    ```bash
    git clone https://github.com/yourusername/todo-app-pyside6.git
    cd todo-app-pyside6
    ```

## 🚀 اجرا

برای اجرای برنامه، دستور زیر را در ترمینال وارد کنید:

```bash
python main.py
```

## 📚 نحوه استفاده

1. **اجرای برنامه:** برنامه را با دستور بالا اجرا کنید.
2. **افزودن وظیفه:** در فیلد متنی، وظیفه جدید را وارد کرده و روی دکمه **"Add Task"** کلیک کنید.
3. **حذف وظیفه:** وظیفه مورد نظر را از لیست انتخاب کرده و روی دکمه **"Remove Selected Task"** کلیک کنید.

## 🗂️ ساختار پروژه

- `main.py` : فایل اصلی حاوی کد برنامه.
- `README.md` : فایل راهنما و توضیحات پروژه.

## 💻 کد اصلی

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QListWidget, 
    QPushButton, QLineEdit, QMessageBox
)

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # تنظیمات پنجره اصلی
        self.setWindowTitle("To-Do List App")
        self.setGeometry(300, 300, 400, 300)
        # ویجت مرکزی
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # لایه‌بندی اصلی
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        # لیست وظایف
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        # لایه‌بندی افقی برای ورودی و دکمه‌ها
        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)
        # ورودی متن برای افزودن وظایف
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("یک وظیفه جدید وارد کنید...")
        self.input_layout.addWidget(self.task_input)
        # دکمه افزودن
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.add_button)
        # دکمه حذف
        self.remove_button = QPushButton("Remove Selected Task")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

    def add_task(self):
        """افزودن وظیفه جدید به لیست."""
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "وظیفه نمی‌تواند خالی باشد!")

    def remove_task(self):
        """حذف وظیفه انتخاب شده از لیست."""
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Warning", "هیچ وظیفه‌ای انتخاب نشده است!")

# تابع اصلی برای اجرای برنامه
def main():
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

## 📜 مجوز

این پروژه تحت مجوز [MIT](LICENSE) منتشر شده است.

## 📨 ارتباط با ما

در صورت وجود هرگونه سوال یا پیشنهاد، لطفاً از طریق ایمیل [your.email@example.com](mailto:your.email@example.com) با ما در ارتباط باشید.

## 🙏 سپاسگزاری

از تمامی کسانی که در توسعه این پروژه همکاری کرده‌اند، سپاسگزاریم.

## 🌐 انتخاب زبان

[![English](https://img.shields.io/badge/Language-English-blue)](README.md) [![فارسی](https://img.shields.io/badge/Language-فارسی-green)](README.fa.md)