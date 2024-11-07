import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

class BookRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Recommendation App")
        self.root.geometry("400x300")

        # Load data
        self.load_books()

        # Genre selection
        self.genre_label = tk.Label(root, text="Select Genre:")
        self.genre_label.pack(pady=5)

        self.genre_combo = ttk.Combobox(root, values=self.genres)
        self.genre_combo.pack(pady=5)

        # Recommend button
        self.recommend_button = tk.Button(root, text="Recommend Books", command=self.recommend_books)
        self.recommend_button.pack(pady=10)

        # Results area
        self.result_area = tk.Text(root, wrap="word", height=10, width=40)
        self.result_area.pack(pady=10)
        self.result_area.config(state="disabled")  # Read-only initially

    def load_books(self):
        """Load book data from a CSV file."""
        self.books_df = pd.read_csv('resource/books.csv')
        self.genres = self.books_df['genre'].unique().tolist()

    def recommend_books(self):
        """Recommend books based on the selected genre."""
        selected_genre = self.genre_combo.get()

        if not selected_genre:
            messagebox.showwarning("Warning", "Please select a genre.")
            return

        # Filter books by genre
        filtered_books = self.books_df[self.books_df['genre'] == selected_genre]

        if not filtered_books.empty:
            result = f"Books in the genre '{selected_genre}':\n\n"
            result += "\n".join(f"- {row['title']} by {row['author']}" for _, row in filtered_books.iterrows())
        else:
            result = "No books found for this genre."

        # Display results
        self.result_area.config(state="normal")  # Enable text area for writing
        self.result_area.delete(1.0, tk.END)  # Clear previous content
        self.result_area.insert(tk.END, result)
        self.result_area.config(state="disabled")  # Disable text area to make it read-only

# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BookRecommendationApp(root)
    root.mainloop()
