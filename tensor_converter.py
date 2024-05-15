import numpy as np

class TensorConverter:
    """
    This class is used to restore a complete elastic matrix from independent matrix elements.
    """
    def converter(self, tensor_list, label):
        if label == "cubic":
            return self.__cubic_crystal_tensor(tensor_list, label)
        elif label == "tetragonal 1":
            return self.__tetragonal1_crystal_tensor(tensor_list, label)
        elif label == "tetragonal 2":
            return self.__tetragonal2_crystal_tensor(tensor_list, label)
        elif label == "orthorhomabic":
            return self.__orthorhomabic_crystal_tensor(tensor_list, label)
        elif label == "hexagonal":
            return self.__hexagonal_crystal_tensor(tensor_list, label)
        elif label == "trigonal 1":
            return self.__trigonal1_crystal_tensor(tensor_list, label)
        elif label == "trigonal 2":
            return self.__trigonal2_crystal_tensor(tensor_list, label)
        else:
            raise ValueError("Unsupported tensor label")
        
    def __cubic_crystal_tensor(self, tensor_list, label):
        if label == "cubic":
            C11, C12, C44 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[2, 2] = C11
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C44
            voigt_matrix[5, 5] = C44
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C12
            voigt_matrix[2, 0] = C12
            voigt_matrix[1, 2] = C12
            voigt_matrix[2, 1] = C12
            
            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")
    
    def __tetragonal1_crystal_tensor(self, tensor_list, label):
        if label == "tetragonal 1":
            C11, C12, C13, C33, C44, C66 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2), round(tensor_list[5]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C13
            voigt_matrix[2, 1] = C13
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C44
            voigt_matrix[5, 5] = C66
            
            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")
        
    def __tetragonal2_crystal_tensor(self, tensor_list, label):
        if label == "tetragonal 2":
            C11, C12, C13, C16, C33, C44, C66 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2), round(tensor_list[5]*100,2), round(tensor_list[6]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C13
            voigt_matrix[2, 1] = C13
            voigt_matrix[0, 5] = C16
            voigt_matrix[5, 0] = C16
            voigt_matrix[1, 5] = -C16
            voigt_matrix[5, 1] = -C16
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C44
            voigt_matrix[5, 5] = C66
            
            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")

    def __orthorhomabic_crystal_tensor(self, tensor_list, label):
        if label == "orthorhomabic":
            C11, C12, C13, C22, C23, C33, C44, C55, C66 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2), round(tensor_list[5]*100,2), round(tensor_list[6]*100,2), round(tensor_list[7]*100,2), round(tensor_list[8]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C22
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C55
            voigt_matrix[5, 5] = C66
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C23
            voigt_matrix[2, 1] = C23

            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")
        
    def __hexagonal_crystal_tensor(self, tensor_list, label):
        if label == "hexagonal":
            C11, C12, C13, C33, C55 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C13
            voigt_matrix[2, 1] = C13
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C55
            voigt_matrix[4, 4] = C55
            voigt_matrix[5, 5] = round(0.5*(C11-C12), 2)
            
            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")
    
    def __trigonal1_crystal_tensor(self, tensor_list, label):
        if label == "trigonal 1":
            C11, C12, C13, C14, C33, C44 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2), round(tensor_list[5]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C13
            voigt_matrix[2, 1] = C13
            voigt_matrix[0, 3] = C14
            voigt_matrix[3, 0] = C14
            voigt_matrix[1, 3] = -C14
            voigt_matrix[3, 1] = -C14
            voigt_matrix[4, 5] = C13
            voigt_matrix[5, 4] = C13
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C44
            voigt_matrix[5, 5] = round(0.5*(C11-C12), 2)

            return voigt_matrix.tolist()
        else:
            raise ValueError("Unsupported tensor label")
        
    def __trigonal2_crystal_tensor(self, tensor_list, label):
        if label == "trigonal 2":
            C11, C12, C13, C14, C25, C33, C44 = round(tensor_list[0]*100,2), round(tensor_list[1]*100,2), round(tensor_list[2]*100,2), round(tensor_list[3]*100,2), round(tensor_list[4]*100,2), round(tensor_list[5]*100,2), round(tensor_list[6]*100,2)
            voigt_matrix = np.zeros((6, 6))

            # Assigning values to Voigt notation positions
            voigt_matrix[0, 0] = C11
            voigt_matrix[1, 1] = C11
            voigt_matrix[0, 1] = C12
            voigt_matrix[1, 0] = C12
            voigt_matrix[0, 2] = C13
            voigt_matrix[2, 0] = C13
            voigt_matrix[1, 2] = C13
            voigt_matrix[2, 1] = C13
            voigt_matrix[0, 3] = C14
            voigt_matrix[3, 0] = C14
            voigt_matrix[1, 3] = -C14
            voigt_matrix[3, 1] = -C14
            voigt_matrix[4, 5] = C13
            voigt_matrix[5, 4] = C13
            voigt_matrix[0, 4] = -C25
            voigt_matrix[4, 0] = -C25
            voigt_matrix[1, 4] = C25
            voigt_matrix[4, 1] = C25
            voigt_matrix[3, 5] = C25
            voigt_matrix[5, 3] = C25
            voigt_matrix[2, 2] = C33
            voigt_matrix[3, 3] = C44
            voigt_matrix[4, 4] = C44
            voigt_matrix[5, 5] = round(0.5*(C11-C12), 2)

            return voigt_matrix.tolist()