# Week 7 Assignment: Hands-On Lab - Shopping List Manager

A three-stage Python lab on working with lists: warm up, build a menu-driven manager, then generate a report.

## Files

- `list_warmup.py` - Creates a list of fruits and demonstrates index access, `.append()`, `.remove()` and `len()`.
- `shopping_list.py` - A menu-driven shopping list manager (add / remove / show / done) that never crashes.
- `list_report.py` - Prints a numbered list, counts names longer than 4 letters, and finds the longest name using a loop.
- `screenshots/` - Screenshots of each program running.

## Why check `in` before `.remove()`?

Calling `.remove()` on an item that is not in the list raises a `ValueError` and crashes the program. Checking with `in` first lets us handle the missing item gracefully by printing a friendly message instead. This makes the program safer and more reliable for users who may mistype an item name.
