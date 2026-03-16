import { NativeStackScreenProps } from "@react-navigation/native-stack";
import { useState } from "react";
import {
  Alert,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";

import { RootStackParamList } from "../navigation/AppNavigator";
import { useRegistroStore } from "../store/registroStore";

type Props = NativeStackScreenProps<RootStackParamList, "CadastroRegistro">;

export function CadastroRegistroScreen({ navigation }: Props) {
  const salvarRegistro = useRegistroStore((state) => state.salvarRegistro);
  const loading = useRegistroStore((state) => state.loading);

  const [idPaciente, setIdPaciente] = useState("");
  const [idVacina, setIdVacina] = useState("");
  const [numeroDose, setNumeroDose] = useState("");
  const [dataAplicacao, setDataAplicacao] = useState("");
  const [lote, setLote] = useState("");
  const [nomeVacinador, setNomeVacinador] = useState("");

  const limparFormulario = () => {
    setIdPaciente("");
    setIdVacina("");
    setNumeroDose("");
    setDataAplicacao("");
    setLote("");
    setNomeVacinador("");
  };

  const onSubmit = async () => {
    if (
      !idPaciente ||
      !idVacina ||
      !numeroDose ||
      !dataAplicacao ||
      !lote ||
      !nomeVacinador
    ) {
      Alert.alert(
        "Campos obrigatorios",
        "Preencha todos os campos do formulario.",
      );
      return;
    }

    try {
      await salvarRegistro({
        id_paciente: Number(idPaciente),
        id_vacina: Number(idVacina),
        numero_dose: Number(numeroDose),
        data_aplicacao: dataAplicacao,
        lote,
        nome_vacinador: nomeVacinador,
      });

      Alert.alert("Sucesso", "Registro de vacinacao salvo com sucesso.");
      limparFormulario();
    } catch {
      Alert.alert("Erro", "Nao foi possivel salvar o registro.");
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.heading}>Cadastro de Dose Aplicada</Text>

      <View style={styles.formGroup}>
        <Text style={styles.label}>ID Paciente</Text>
        <TextInput
          style={styles.input}
          value={idPaciente}
          onChangeText={setIdPaciente}
          keyboardType="numeric"
        />
      </View>

      <View style={styles.formGroup}>
        <Text style={styles.label}>ID Vacina</Text>
        <TextInput
          style={styles.input}
          value={idVacina}
          onChangeText={setIdVacina}
          keyboardType="numeric"
        />
      </View>

      <View style={styles.formGroup}>
        <Text style={styles.label}>Numero da Dose</Text>
        <TextInput
          style={styles.input}
          value={numeroDose}
          onChangeText={setNumeroDose}
          keyboardType="numeric"
        />
      </View>

      <View style={styles.formGroup}>
        <Text style={styles.label}>Data de Aplicacao (AAAA-MM-DD)</Text>
        <TextInput
          style={styles.input}
          value={dataAplicacao}
          onChangeText={setDataAplicacao}
          autoCapitalize="none"
        />
      </View>

      <View style={styles.formGroup}>
        <Text style={styles.label}>Lote</Text>
        <TextInput style={styles.input} value={lote} onChangeText={setLote} />
      </View>

      <View style={styles.formGroup}>
        <Text style={styles.label}>Nome do Vacinador</Text>
        <TextInput
          style={styles.input}
          value={nomeVacinador}
          onChangeText={setNomeVacinador}
        />
      </View>

      <Pressable
        style={styles.primaryButton}
        onPress={onSubmit}
        disabled={loading}
      >
        <Text style={styles.primaryButtonText}>
          {loading ? "Salvando..." : "Salvar Registro"}
        </Text>
      </Pressable>

      <Pressable
        style={styles.secondaryButton}
        onPress={() => navigation.navigate("Historico")}
      >
        <Text style={styles.secondaryButtonText}>Ver Historico</Text>
      </Pressable>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: "#F0F4F8",
    gap: 8,
  },
  heading: {
    fontSize: 20,
    fontWeight: "700",
    marginBottom: 12,
    color: "#102A43",
  },
  formGroup: {
    marginBottom: 4,
  },
  label: {
    fontSize: 14,
    marginBottom: 6,
    color: "#334E68",
  },
  input: {
    borderWidth: 1,
    borderColor: "#BCCCDC",
    backgroundColor: "#FFFFFF",
    borderRadius: 10,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  primaryButton: {
    marginTop: 12,
    backgroundColor: "#0E7490",
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: "center",
  },
  primaryButtonText: {
    color: "#FFFFFF",
    fontWeight: "700",
  },
  secondaryButton: {
    marginTop: 8,
    borderWidth: 1,
    borderColor: "#0E7490",
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: "center",
  },
  secondaryButtonText: {
    color: "#0E7490",
    fontWeight: "700",
  },
});
