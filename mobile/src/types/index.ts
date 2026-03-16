export type Paciente = {
  id: number;
  nome: string;
  cpf: string;
  data_nascimento: string;
};

export type Vacina = {
  id: number;
  nome_comercial: string;
  grupo_doenca: string;
};

export type RegistroVacinacaoPayload = {
  id_paciente: number;
  id_vacina: number;
  numero_dose: number;
  data_aplicacao: string;
  lote: string;
  nome_vacinador: string;
};

export type RegistroVacinacao = RegistroVacinacaoPayload & {
  id: number;
};

export type RegistroHistorico = {
  id: number;
  numero_dose: number;
  data_aplicacao: string;
  lote: string;
  nome_vacinador: string;
  vacina: Vacina;
};

export type HistoricoPacienteResponse = {
  paciente: Paciente;
  registros: RegistroHistorico[];
};
