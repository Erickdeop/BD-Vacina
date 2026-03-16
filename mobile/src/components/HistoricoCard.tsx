import { StyleSheet, Text, View } from "react-native";

import { RegistroHistorico } from "../types";

type Props = {
  item: RegistroHistorico;
};

export function HistoricoCard({ item }: Props) {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{item.vacina.nome_comercial}</Text>
      <Text style={styles.subtitle}>Grupo: {item.vacina.grupo_doenca}</Text>
      <Text style={styles.text}>Dose: {item.numero_dose}</Text>
      <Text style={styles.text}>Data: {item.data_aplicacao}</Text>
      <Text style={styles.text}>Lote: {item.lote}</Text>
      <Text style={styles.text}>Vacinador: {item.nome_vacinador}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: "#FFFFFF",
    borderRadius: 12,
    padding: 14,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: "#D9E2EC",
  },
  title: {
    fontSize: 16,
    fontWeight: "700",
    color: "#102A43",
  },
  subtitle: {
    marginTop: 2,
    marginBottom: 8,
    fontSize: 12,
    color: "#486581",
  },
  text: {
    fontSize: 14,
    color: "#243B53",
    marginBottom: 2,
  },
});
