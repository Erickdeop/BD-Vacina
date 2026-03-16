import { create } from "zustand";

import { api } from "../services/api";
import {
  HistoricoPacienteResponse,
  RegistroHistorico,
  RegistroVacinacaoPayload,
} from "../types";

type RegistroState = {
  pacienteId: number | null;
  pacienteNome: string;
  registros: RegistroHistorico[];
  loading: boolean;
  error: string | null;
  salvarRegistro: (payload: RegistroVacinacaoPayload) => Promise<void>;
  carregarHistorico: (pacienteId: number) => Promise<void>;
};

export const useRegistroStore = create<RegistroState>((set) => ({
  pacienteId: null,
  pacienteNome: "",
  registros: [],
  loading: false,
  error: null,

  salvarRegistro: async (payload) => {
    set({ loading: true, error: null });
    try {
      await api.post("/registros", payload);
      set({ loading: false });
    } catch {
      set({
        loading: false,
        error: "Falha ao salvar o registro de vacinacao.",
      });
    }
  },

  carregarHistorico: async (pacienteId) => {
    set({ loading: true, error: null });
    try {
      const response = await api.get<HistoricoPacienteResponse>(
        `/pacientes/${pacienteId}/historico`,
      );
      set({
        loading: false,
        pacienteId,
        pacienteNome: response.data.paciente.nome,
        registros: response.data.registros,
      });
    } catch {
      set({
        loading: false,
        pacienteId,
        pacienteNome: "",
        registros: [],
        error: "Nao foi possivel carregar o historico do paciente.",
      });
    }
  },
}));
