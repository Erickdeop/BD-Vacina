import { useState } from "react";
import {
  FlatList,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";

import { HistoricoCard } from "../components/HistoricoCard";
import { useRegistroStore } from "../store/registroStore";

export function HistoricoScreen() {
  const [pacienteIdInput, setPacienteIdInput] = useState("");

  const carregarHistorico = useRegistroStore(
    (state) => state.carregarHistorico,
  );
  const pacienteNome = useRegistroStore((state) => state.pacienteNome);
  const registros = useRegistroStore((state) => state.registros);
  const loading = useRegistroStore((state) => state.loading);
  const error = useRegistroStore((state) => state.error);

  const onBuscar = async () => {
    if (!pacienteIdInput) {
      return;
    }
    await carregarHistorico(Number(pacienteIdInput));
  };

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Historico de Vacinacao</Text>

      <View style={styles.searchRow}>
        <TextInput
          style={styles.input}
          value={pacienteIdInput}
          onChangeText={setPacienteIdInput}
          keyboardType="numeric"
          placeholder="Informe o ID do paciente"
        />
        <Pressable style={styles.button} onPress={onBuscar}>
          <Text style={styles.buttonText}>{loading ? "..." : "Buscar"}</Text>
        </Pressable>
      </View>

      {pacienteNome ? (
        <Text style={styles.patientName}>Paciente: {pacienteNome}</Text>
      ) : null}
      {error ? <Text style={styles.error}>{error}</Text> : null}

      <FlatList
        data={registros}
        keyExtractor={(item) => String(item.id)}
        renderItem={({ item }) => <HistoricoCard item={item} />}
        contentContainerStyle={styles.listContent}
        ListEmptyComponent={
          !loading ? (
            <Text style={styles.empty}>Nenhum registro para exibir.</Text>
          ) : null
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#F0F4F8",
  },
  heading: {
    fontSize: 20,
    fontWeight: "700",
    color: "#102A43",
    marginBottom: 12,
  },
  searchRow: {
    flexDirection: "row",
    gap: 8,
    marginBottom: 12,
  },
  input: {
    flex: 1,
    borderWidth: 1,
    borderColor: "#BCCCDC",
    backgroundColor: "#FFFFFF",
    borderRadius: 10,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  button: {
    backgroundColor: "#0E7490",
    borderRadius: 10,
    justifyContent: "center",
    paddingHorizontal: 16,
  },
  buttonText: {
    color: "#FFFFFF",
    fontWeight: "700",
  },
  patientName: {
    marginBottom: 8,
    color: "#243B53",
    fontWeight: "600",
  },
  error: {
    color: "#B42318",
    marginBottom: 8,
  },
  listContent: {
    paddingBottom: 24,
  },
  empty: {
    color: "#627D98",
    marginTop: 16,
    textAlign: "center",
  },
});
