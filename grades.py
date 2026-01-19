import pandas as pd

def main():
    df = pd.read_csv('data/grades.csv')  
    print("Columns in the dataset:", df.columns)

    num_students = len(df)
    print(f"Number of students: {num_students}")

    avg_final_grade = df['final grade'].mean() 
    print(f"Average final grade: {avg_final_grade:.2f}")

    lowest_final_grade = df['final grade'].min()  
    print(f"Lowest final grade: {lowest_final_grade}")

    avg_grades = df.mean(numeric_only=True)  
    column_with_lowest_avg = avg_grades.idxmin()
    print(f"Column with the lowest average grade: {column_with_lowest_avg}")

    student_15_sss = df.loc[14, 'SSS']  
    print(f"Student 15’s SSS grade: {student_15_sss}")

    student_10_highest_grade = df.loc[9, ['SSS', 'final grade', 'midterm_grade']].max()  # Adjust column names if necessary
    print(f"Student 10’s highest grade: {student_10_highest_grade}")

if __name__ == '__main__':
    main()
