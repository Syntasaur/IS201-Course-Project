"""Entry point for the IS201 course project scaffold."""

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("IS201 Course Project")
    root.geometry("640x360")

    message = tk.Label(
        root,
        text="Project idea is not defined yet.",
        font=("Segoe UI", 14),
    )
    message.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
