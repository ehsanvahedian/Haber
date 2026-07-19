export type UniverseItemType =
  | "word"
  | "number"
  | "income"
  | "debt"
  | "task"
  | "transaction"
  | "icon";

export type UniverseItem = {
  id: string;
  type: UniverseItemType;
  content: string;
  x: number;
  y: number;
  rotation: number;
  delay: number;
  duration: number;
};