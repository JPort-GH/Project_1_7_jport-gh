"""
File: acronym_manager.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Manages a collection of Acronym objects. Handles adding, searching,
    listing, saving, and loading acronym data for the VSP Acronym Assistant.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
from acronym import Acronym
import json

class AcronymManager:
    """
    Manages a list of Acronym objects and provides operations for them.
    """

    def __init__(self):
        """Initialize the manager with an empty acronym list."""
        self.acronyms = []

    # Methods will be added in later milestones
def add_acronym(self, short: str, definition: str, category: str):
        """
        Add a new acronym to the list.

        Parameters:
            short (str): The acronym text.
            definition (str): The full meaning.
            category (str): The category it belongs to.
        """
        new_acronym = Acronym(short, definition, category)
        self.acronyms.append(new_acronym)

    def search_acronym(self, short: str):
        """
        Search for an acronym by its short text (case-insensitive).

        Parameters:
            short (str): The acronym text to search for.

        Returns:
            Acronym or None: The matching acronym, if found.
        """
        short = short.lower()
        for acronym in self.acronyms:
            if acronym.short.lower() == short:
                return acronym
        return None

