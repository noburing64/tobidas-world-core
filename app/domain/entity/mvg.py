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
        
        subprocess.run(command)
        
    def ComputeFeatures(self):
        command = [
            self.__getCommandPath("ComputeFeatures"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-o", self.__matches_dir,
            "-m", "SIFT",
            "-f", "1"
        ]
        
        subprocess.run(command)
        
    def ComputeMatches(self):
        command = [
            self.__getCommandPath("ComputeMatches"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-o", self.__matches_dir + "/matches.putative.bin",
            "-f", "1",
            "-n", "ANNL2"
        ]
        
        subprocess.run(command)
        
    def GeometricFilter(self, geo):
        command = [
            self.__getCommandPath("GeometricFilter"),
            "-i", self.__matches_dir + "/sfm_data.json",
            "-m", self.__matches_dir + "/matches.putative.bin",
            "-g", geo,
            "-o", self.__matches_dir + f"/matches.{geo}.bin"
        ]
        
        subprocess.run(command)
        
    def StartSfm(self, engine="INCREMENTAL"):
        if engine not in ["GLOBAL", "INCREMENTAL"]:
            raise Exception
        
        command = [
            self.__getCommandPath("SfM"),
            "--sfm_engine", engine,
            "--input_file", self.__matches_dir + "/sfm_data.json",
            "--output_dir", self.__reconstruction_dir,
            "--match_dir", self.__matches_dir + ("/matches.e.bin" if engine == "GLOBAL" else "")
        ]
        
        subprocess.run(command)
        
    def ComputeSfmDataColor(self, dir_type="global"):
        reconstruction_dir = self.__reconstruction_global_dir if dir_type == "global" else self.__reconstruction_dir
        command = [
            self.__getCommandPath("ComputeSfM_DataColor"),
            "-i", reconstruction_dir + "/sfm_data.bin",
            "-o", self.__reconstruction_dir + "/colorized.ply"
        ]
        
        subprocess.run(command)
        
    def ComputeStructureFromKnownPoses(self):
        command = [
            self.__getCommandPath("ComputeStructureFromKnownPoses"),
            "-i", self.__reconstruction_global_dir + "/sfm_data.bin",
            "-m", self.__matches_dir,
            "-o", self.__reconstruction_global_dir + "/robust.ply"
        ]
        
        subprocess.run(command)