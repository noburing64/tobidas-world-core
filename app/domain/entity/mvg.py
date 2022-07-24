import subprocess

class Mvg:
    def __init__(
        self,
        input_dir,
        command_dir,
        matches_dir,
        reconstruction_dir,
        reconstruction_global_dir,
        camera_file_params
    ):
        self.__input_dir = input_dir
        self.__command_dir = command_dir
        self.__matches_dir = matches_dir
        self.__reconstruction_dir = reconstruction_dir
        self.__reconstruction_global_dir = reconstruction_global_dir
        self.__camera_file_params = camera_file_params
        
    def __getCommandPath(self, command: str):
        return self.__command_dir + "/openMVG_main_" + command
        
    def SfmInitImageListing(self):
        command = [
            self.__getCommandPath("SfMInit_ImageListing"),
            "-i", self.__input_dir,
            "-o", self.__matches_dir,
            "-d", self.__camera_file_params,
            "-c", "3"
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def ComputeFeatures(self):
        command = [
            self.__getCommandPath("ComputeFeatures"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-o", self.__matches_dir,
            "-m", "SIFT",
            "-f", "1"
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def ComputeMatches(self):
        command = [
            self.__getCommandPath("ComputeMatches"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-o", self.__matches_dir + "/matches.putative.bin",
            "-f", "1",
            "-n", "ANNL2"
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def GeometricFilter(self, geo):
        command = [
            self.__getCommandPath("GeometricFilter"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-m", self.__matches_dir + "/matches.putative.bin",
            "-g", geo,
            "-o", self.__matches_dir + f"/matches.{geo}.bin"
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def StartSfm(self, engine):
        command = [
            self.__getCommandPath("SfM"),
            "--sfm_engine", "GLOBAL" if engine == "global" else "INCREMENTAL",
            "--input_file", self.__matches_dir + "/sfm_data.json",
            "--output_dir",
            self.__reconstruction_global_dir if engine == "global" else self.__reconstruction_dir,
            "--match_file" if engine == "global" else "--match_dir",
            self.__matches_dir + ("/matches.e.bin" if engine == "global" else "")
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def ComputeSfmDataColor(self, dir_type=""):
        reconstruction_dir = self.__reconstruction_global_dir if dir_type == "global" else self.__reconstruction_dir
        command = [
            self.__getCommandPath("ComputeSfM_DataColor"),
            "-i", reconstruction_dir + "/sfm_data.bin",
            "-o", reconstruction_dir + "/colorized.ply"
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL)
        
    def ComputeStructureFromKnownPoses(self, dir_type=""):
        command = [
            self.__getCommandPath("ComputeStructureFromKnownPoses"),
            "-i", 
            (self.__reconstruction_global_dir if dir_type == "global" else self.__reconstruction_dir)+ "/sfm_data.bin",
            "-m", self.__matches_dir,
            "-o",
            (self.__reconstruction_global_dir if dir_type == "global" else self.__reconstruction_dir)+ "/robust.ply"
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL)