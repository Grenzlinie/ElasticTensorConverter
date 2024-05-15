# ElasticTensorConverter
The `ElasticTensorConverter` class is designed to restore a complete elastic matrix from independent matrix elements. It is particularly useful in material science and engineering applications where crystal tensor data needs to be converted into a structured format.

## Usage

1. **Initialization:**

   ```python
   converter = TensorConverter()
   ```

   The `TensorConverter` class does not require any parameters during initialization.

2. **Conversion:**

   To perform a conversion, use the `converter` method:

   ```python
   tensor_list = [C11, C12, C44]  # Example tensor data
   label = "cubic"  # Specify the crystal system label

   elastic_matrix = converter.converter(tensor_list, label)
   ```

   - `tensor_list`: List of independent matrix elements.
   - `label`: Label indicating the crystal system for conversion.

   Supported crystal system labels are:
   - "cubic"
   - "tetragonal 1"
   - "tetragonal 2"
   - "orthorhombic"
   - "hexagonal"
   - "trigonal 1"
   - "trigonal 2"

3. **Returned Matrix Format:**

   The `converter` method returns the elastic matrix in Voigt notation as a Python list.

## Conversion Methods

- `__cubic_crystal_tensor(tensor_list, label)`: Converts tensor data for the cubic crystal system.
- `__tetragonal1_crystal_tensor(tensor_list, label)`: Converts tensor data for the first type of tetragonal crystal system.
- `__tetragonal2_crystal_tensor(tensor_list, label)`: Converts tensor data for the second type of tetragonal crystal system.
- `__orthorhomabic_crystal_tensor(tensor_list, label)`: Converts tensor data for the orthorhombic crystal system.
- `__hexagonal_crystal_tensor(tensor_list, label)`: Converts tensor data for the hexagonal crystal system.
- `__trigonal1_crystal_tensor(tensor_list, label)`: Converts tensor data for the first type of trigonal crystal system.
- `__trigonal2_crystal_tensor(tensor_list, label)`: Converts tensor data for the second type of trigonal crystal system.

These methods are automatically called by the `converter` method based on the specified crystal system label.

## Example

```python
converter = TensorConverter()
tensor_list = [1, 2, 3]  # Example tensor data
label = "cubic"  # Specify the crystal system label

elastic_matrix = converter.converter(tensor_list, label)
print(elastic_matrix)
```

In this example, the `converter` method is used to convert tensor data for the cubic crystal system, resulting in an elastic matrix in Voigt notation.