import subprocess

class Mvs:
    def __init__(
        self,
        command_dir,
        command_bin_dir,
        reconstruction_dir,
        image_dir
    ):
        self.__command_dir = command_dir
        self.__command_bin_dir = command_bin_dir        
        self.__reconstruction_dir = reconstruction_dir
        self.__image_dir = image_dir
        
    def __getCommandPath(self, command: str):
        return self.__command_dir + "/openMVG_main_" + command
    
    def __getCommandBinPath(self, command: str):
        return self.__command_bin_dir + "/" + command
        
    def OpenMVG2OpenMVS(self) -> subprocess.CompletedProcess:
        command = [
            self.__getCommandPath("openMVG2openMVS"),
            "-i", self.__reconstruction_dir + "/sfm_data.bin",
            "-o", self.__reconstruction_dir + "/scene.mvs",
            "-d", self.__image_dir
        ]
        
        return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    def DensifyPointCloud(self) -> subprocess.CompletedProcess:
        command = [
            self.__getCommandBinPath("DensifyPointCloud"),
            self.__reconstruction_dir + "/scene.mvs"
        ]
        
        return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    def ReconstructMesh(self) -> subprocess.CompletedProcess:
        command = [
            self.__getCommandBinPath("ReconstructMesh"),
            self.__reconstruction_dir + "/scene_dense.mvs"
        ]
        
        return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    def RefineMesh(self) -> subprocess.CompletedProcess:
        command = [
            self.__getCommandBinPath("RefineMesh"),
            self.__reconstruction_dir + "/scene_dense_mesh.mvs",
            "--scales", "10",
            "--scale-step", "0.8",
            "--resolution-level", "3"
        ]
        
        return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    def TextureMesh(self) -> subprocess.CompletedProcess:
        command = [
            self.__getCommandBinPath("TextureMesh"),
            self.__reconstruction_dir + "/scene_dense_mesh_refine.mvs",
            "--export-type", "obj",
            "-o", self.__reconstruction_dir + "/model_data"
        ]
        
        return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)