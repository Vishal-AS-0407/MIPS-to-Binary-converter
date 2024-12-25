# MIPS to Binary Converter 🔢

This is a simple Python-based **MIPS to Binary Converter** that helps beginners learn and work with MIPS assembly language. The program performs the following key functions:

- **Converts MIPS instructions** into the corresponding **machine code** in binary format.
- **Identifies errors** in incorrectly formatted instructions, providing specific feedback on the issue.
- **Provides corrected sample formats** to help users understand and correct their MIPS instructions.
- Designed for **beginners** who are learning MIPS assembly, making it an excellent educational tool.

The program supports a variety of MIPS instructions, and it continuously validates the syntax to ensure proper formatting, helping users gradually improve their understanding of the MIPS instruction set.

---


## 📋 Requirements

- Python 3.x

---

## 🚀 How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mips-instruction-set-simulator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mips-instruction-set-simulator
   ```

3. Run the `main.py` file:
   ```bash
   python main.py
   ```

4. Enter your MIPS instruction when prompted. For example:
   ```text
   Enter your MIPS instruction:
   add $t0, $t1, $t2
   ```

   The program will process the instruction and display the corresponding machine code.

5. You can input additional instructions or type 'no' when prompted to exit the program.

---


## ⚙️ How the Program Works

1. The program continuously asks for MIPS instructions until you decide to stop.
2. Instructions should be entered in lowercase (e.g., `add $t0, $t1, $t2`).
3. The program validates the syntax and prints the corresponding machine code in binary format if the instruction is valid.
4. If the input is invalid, it will prompt you to correct the format.

---

## 💻 Example

**Input:**
```
Enter your MIPS instruction:
add $t0, $t1, $t2
```

**Output:**
```
000000 01001 01010 01000 00000 100000
```
### Sample Output
![image](https://github.com/user-attachments/assets/f1a07530-a1ef-4a2e-a678-9e5bbc9d6e7e)

---
### 🌟 **Show Your Support!**  

If you find this project helpful, give it a ⭐ on GitHub and share it with others! 😊  
