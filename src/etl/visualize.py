import matplotlib.pyplot as plt

def genre_distribution(df):
    # Group the data by genre and count the number of books
    genre_counts = df.groupby('Genre').size()
    
    # Plotting - Bar
    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='bar')
    plt.title('Number of Books by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Books')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    #Plotting - Pie
    plt.figure(figsize=(8, 8))
    genre_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Books by Genre')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()