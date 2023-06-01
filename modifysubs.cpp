#include <iostream>
#include <fstream>
#include <regex>
#include <map>
#include <ass/ass.h>

void modifySubs(const std::string& subfile) {
    ASS_Library* assLibrary = ass_library_init(); // Initialize the libass library
    if (!assLibrary) {
        std::cout << "Failed to initialize libass library" << std::endl;
        return;
    }

    ASS_Renderer* assRenderer = ass_renderer_init(assLibrary); // Initialize the renderer
    if (!assRenderer) {
        ass_library_done(assLibrary);
        std::cout << "Failed to initialize libass renderer" << std::endl;
        return;
    }

    ASS_Track* assTrack = ass_read_file(assLibrary, subfile.c_str(), nullptr); // Read the SSA file
    if (!assTrack) {
        ass_renderer_done(assRenderer);
        ass_library_done(assLibrary);
        std::cout << "Failed to load SSA file" << std::endl;
        return;
    }

    const std::map<std::string, std::string> WORDS = {
        // Define your replacement mappings here
        // Example: { "word1", "replacement1" },
        //          { "word2", "replacement2" },
    };

    for (int i = 0; i < assTrack->n_events; i++) {
        ASS_Event* event = assTrack->events + i;
        std::string text = event->Text;

        for (const auto& word : WORDS) {
            text = std::regex_replace(text, std::regex(word.first, std::regex_constants::icase), word.second);
        }

        event->Text = ass_strdup(text.c_str());
    }

    // Save the modified subtitles
    ass_write_file(assTrack, "[Delocalized].ass", nullptr);

    // Cleanup
    ass_free_track(assTrack);
    ass_renderer_done(assRenderer);
    ass_library_done(assLibrary);
}

int main() {
    std::string subfile = "your_subtitles.ass";
    modifySubs(subfile);
    return 0;
}