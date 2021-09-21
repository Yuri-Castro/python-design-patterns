"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation ofg video exporting codec
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folde

        Args:
            folder (pathlib.Path): folder path
        """


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print('Preparing video data for lossless export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for lossless format to {folder}.')


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with baseline profile."""


    def prepare_export(self, video_data):
        print('Preparing video data for H.264 (Baseline) export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for H.264 (Baseline) format to {folder}.')


class H264Hi422PVideoExporter(VideoExporter):
    """H2.64 video exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for H.264 (Hi422P) export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for H.264 (Hi422P) format to {folder}.')


class AudioExporter(ABC):
    """Basic representation of audio exporting codec
    """

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the audio data to a folde

        Args:
            folder (pathlib.Path): folder path
        """


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for AAC export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for AAC format to {folder}.')


class WAVAudioExporter(AudioExporter):
    """WAV audio exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for WAV export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for WAV format to {folder}.')

class ExporterFactory(ABC):
    """
        Factory tjat represents a combination of video and audio codecs
        The factory doesn't maintain any of the instances it creates
    """

    def get_video_exporter() -> VideoExporter:
        """Return a new video exporter intance"""

    def get_video_exporter() -> AudioExporter:
        """Return a new video exporter intance"""

class FastExporter(ExporterFactory):
    """
        Factory aimed at providing high speeed, lower quality export.
    """

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """
        Factory aimed at providing slower speeed, high quality export.
    """

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """
        Factory aimed at providing low speeed, master quality export.
    """

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }
    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input('Enter desired quality (low, high, master): ')
        if export_quality in factories:
            return factories[export_quality]
        print(f'Unknown output quality option: {export_quality}. ')


def main(fac: ExporterFactory) -> None:
    """Main function
    """

    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()
    video_exporter: VideoExporter
    audio_exporter: AudioExporter

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = pathlib.Path("./results")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    fac = read_exporter()

    main()

