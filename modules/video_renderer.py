# def render_video(sequence_path):
#     """Trigger Unreal Engine rendering pipeline."""
#     cmd = f'UnrealEditor-Cmd.exe "C:/Path/To/Project.uproject" -MovieRenderPipeline -ExecutePythonScript="{sequence_path}"'
#     os.system(cmd)
#     print("Rendering started...")




import unreal

def render_video(sequence_path, output_file="C:/Users/anmol/Documents/UE_project/output.mp4", resolution_x=1920, resolution_y=1080, frame_rate=30):
    """
    Renders a video from a given sequence in Unreal Engine.
    
    :param sequence_path: Path to the Unreal Engine sequence asset.
    :param output_file: Output path for the rendered video.
    :param resolution_x: Video width.
    :param resolution_y: Video height.
    :param frame_rate: Frame rate of the video.
    """

    # Load the sequence
    level_sequence = unreal.load_asset(sequence_path)
    if not level_sequence:
        print(f"❌ Failed to load sequence: {sequence_path}")
        return

    # Get the Movie Render Queue Subsystem
    render_queue = unreal.MoviePipelineQueueSubsystem().get_queue()
    render_queue.delete_all_jobs()  # Clear any previous jobs

    # Create a new rendering job
    job = render_queue.allocate_new_job(unreal.MoviePipelineExecutorJob)
    job.set_configuration(unreal.MoviePipelineMasterConfig())

    # Set the sequence for rendering
    job.sequence = level_sequence
    job.map = unreal.EditorLevelLibrary.get_editor_world().get_map_name()

    # Configure output settings
    settings = job.get_configuration()
    
    # Set resolution
    settings.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting).resolution = unreal.IntPoint(resolution_x, resolution_y)

    # Set frame rate
    settings.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting).frame_rate = unreal.FrameRate(numerator=frame_rate, denominator=1)

    # Set output file format
    output_setting = settings.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
    output_setting.file_name_format = output_file.replace("\\", "/")  # Ensure proper path format

    # Set render settings (quality, compression)
    render_setting = settings.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_PNG)  # PNG for high quality
    render_setting.compression_quality = 100

    # Start rendering
    executor = unreal.MoviePipelinePIEExecutor()
    executor.queue = render_queue
    executor.execute()

    print(f"✅ Rendering started for {sequence_path}. Output will be saved at {output_file}")

# Example Usage
if __name__ == "__main__":

    render_video(
    r"C:\Users\anmol\Downloads\Pepe_Pro 5.5\Pepe_Pro 5.5\Content\Main_BuiltData.uasset", 
    output_file="C:/Users/anmol/Documents/UE_project/output.mp4", 
    resolution_x=1280,  # Lower resolution
    resolution_y=720,   # Lower resolution
    frame_rate=24       # Lower frame rate for smoother performance
    )
    # render_video("C:\Users\anmol\Downloads\Pepe_Pro 5.5\Pepe_Pro 5.5\Content\Main_BuiltData.uasset", "C:/Users/anmol/Documents/UE_project/output.mp4")
