from OruData.Utils import EnvironmentUtils, RoutingUtils

from .Routers.MainRouter import MainRouter

def main():
  EnvironmentUtils.init(default_theme="Manarola", default_dark_mode=True)
  if EnvironmentUtils.get_debug_mode():
    from OruData.Utils import UserUtils
    UserUtils.force_debug_login('admin')
  set_route()
  EnvironmentUtils.logger().info("Sistema Inicializado com sucesso.")

def set_route():
  EnvironmentUtils.logger().debug(f"LaunchRoute: {RoutingUtils.get_url_hash()}")
  RoutingUtils.launch()


main()