from .reactor import Reactor


def setup(bot):
    bot.add_cog(Reactor(bot))