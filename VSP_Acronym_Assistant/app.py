"""
File: app.py
Author: Janet Portillo (Jport-GH)
Date: 2026-06-25
Purpose:
    Provides the menu system and user interaction for the VSP Acronym Assistant.
    This class handles input, output, and calls to the AcronymManager.
Resources:
    No starter code used. Created for CSCI 1151 Project 1.
"""
from acronym_manager import AcronymManager

class AcronymApp:
    """
    Handles the user interface and menu loop for the application.
    """

    def __init__(self):
        """Initialize the app with an AcronymManager instance."""
        self.manager = AcronymManager()

    # Menu logic will be added in later milestones
