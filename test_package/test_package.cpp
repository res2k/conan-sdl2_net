#include <iostream>
#include <cstdlib>
#include <SDL2/SDL.h>
#include <SDL2/SDL_net.h>

int main(int argc, char *argv[])
{
    const SDL_version * version = SDLNet_Linked_Version();
    std::cout << "SDL2_net version: ";
    std::cout << int(version->major) << ".";
    std::cout << int(version->minor) << ".";
    std::cout << int(version->patch) << std::endl;

    return 0;
}
