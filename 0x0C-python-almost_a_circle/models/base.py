#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv

class Base:
    # Existing code...

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if not list_objs:
                return
            # Write headers
            headers = [attr for attr in vars(list_objs[0]) if not callable(getattr(list_objs[0], attr)) and not attr.startswith("_")]
            writer.writerow(headers)
            # Write data
            for obj in list_objs:
                writer.writerow([getattr(obj, attr) for attr in headers])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        result = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Get the attribute names from the first row
                for row in reader:
                    obj_data = {headers[i]: row[i] for i in range(len(headers))}
                    obj = cls.create(**obj_data)
                    result.append(obj)
        except FileNotFoundError:
            pass  # Return an empty list if the file doesn't exist
        return result
