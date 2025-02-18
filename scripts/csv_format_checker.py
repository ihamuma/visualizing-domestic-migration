import chardet
from csv_detective.explore_csv import routine


def detect_encoding(file_path: str):

    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())

    return result


def inspect_csv(file_path: str):
    inspection_results = routine(
        file_path,
        num_rows=100,  # Value -1 will analyze all lines of your csv, you can change with the number of lines you wish to analyze
        output_mode="LIMITED",  # By default value is LIMITED, if you want result of analysis of all detections made, you can apply an output_mode="ALL"
        # Default False. If True, it will save result output into the same directory than the csv analyzed
        save_results=False,
        # Default False. If True, returned dict will contain a property "profile" indicating profile (min, max, mean, tops...) of every column of you csv
        output_profile=False,
        # Default False. If True, returned dict will contain a property "schema" containing basic [tableschema](https://specs.frictionlessdata.io/table-schema/) of your file. This can be use to validate structure of other csv which should match same structure.
        output_schema=False,
    )

    return inspection_results
