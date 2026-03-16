import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import { CadastroRegistroScreen } from "../screens/CadastroRegistroScreen";
import { HistoricoScreen } from "../screens/HistoricoScreen";

export type RootStackParamList = {
  CadastroRegistro: undefined;
  Historico: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="CadastroRegistro"
        screenOptions={{
          headerStyle: { backgroundColor: "#D9E2EC" },
          headerTintColor: "#102A43",
          contentStyle: { backgroundColor: "#F0F4F8" },
        }}
      >
        <Stack.Screen
          name="CadastroRegistro"
          component={CadastroRegistroScreen}
          options={{ title: "Nova Dose" }}
        />
        <Stack.Screen
          name="Historico"
          component={HistoricoScreen}
          options={{ title: "Historico" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
