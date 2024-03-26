from OruData.Utils import EnvironmentUtils, RoutingUtils

def main():
  EnvironmentUtils.init()
  set_route()
  EnvironmentUtils.logger().info("Sistema Inicializado com sucesso.")

def set_route():
  EnvironmentUtils.logger().debug(f"LaunchRoute: {RoutingUtils.get_url_hash()}")
  RoutingUtils.launch()


main()