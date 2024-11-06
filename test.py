import streamlit as st
import numpy as np

# Sample grid for Sudoku (9x9)
grid = np.zeros((9, 9), dtype=int)

def display_grid(grid):
    for i in range(9):
        for j in range(9):
            grid[i][j] = st.number_input(f"Cell ({i+1},{j+1})", value=grid[i][j], min_value=0, max_value=9, key=f"cell_{i}_{j}")

def solve_sudoku(grid):
    # Add Sudoku solving algorithm here
    pass

st.title("SudokuMaster")

mode = st.radio("Select Mode", ("Interactive", "Auto Solve"))
if mode == "Interactive":
    st.write("Fill the grid to play!")
    display_grid(grid)
else:
    st.write("Auto-solving the Sudoku...")
    solve_sudoku(grid)
    st.write("Solved Grid:")
    st.write(grid)

